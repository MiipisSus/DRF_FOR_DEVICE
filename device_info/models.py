from typing import List, Tuple

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class DeviceBasicInfo(models.Model):
    device_name = models.CharField(default="Device Name", max_length=30)
    device_location = models.CharField(default="Device Location", max_length=30)
    mac_address = models.CharField(null=True, default=None, max_length=30)
    system_boot_time = models.DateTimeField(auto_now=True)
    product_model = models.CharField(null=True, default=None, max_length=30)
    firmware_version = models.CharField(null=True, default=None, max_length=30)
    

class DeviceVideoInfo(models.Model):
    class EncodeTypeChoices(models.IntegerChoices):
        H264 = 0,
        H265 = 1,
        MJPEG = 2
    
    class VideoEncodingChoices(models.IntegerChoices):
        VBR = 0,
        CBR = 1
    
    # mainstream
    enabled_main = models.BooleanField(default=True)
    encode_type_main = models.IntegerField(default=EncodeTypeChoices.H265, choices=EncodeTypeChoices.choices)
    bit_rate_main = models.IntegerField(default=3072, validators=[MinValueValidator(512), MaxValueValidator(8192)])
    quality_main = models.IntegerField(default=40, validators=[MinValueValidator(10), MaxValueValidator(50)])
    url_main = models.CharField(default='v01', max_length=30)
    jpeg_quality_main = models.IntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(80)])
    gop_main = models.IntegerField(default=30, validators=[MinValueValidator(1), MaxValueValidator(90)])
    resolution_width_main = models.IntegerField(default=2592)
    resolution_height_main = models.IntegerField(default=1944)
    frame_rate_main = models.IntegerField(default=30, validators=[MinValueValidator(1), MaxValueValidator(30)])
    video_encoding_main = models.IntegerField(default=VideoEncodingChoices.CBR, choices=VideoEncodingChoices.choices)
    
    # substream
    enabled_sub = models.BooleanField(default=True)
    encode_type_sub = models.IntegerField(default=EncodeTypeChoices.H265, choices=EncodeTypeChoices.choices)
    bit_rate_sub = models.IntegerField(default=1024, validators=[MinValueValidator(256), MaxValueValidator(4096)])
    quality_sub = models.IntegerField(default=40, validators=[MinValueValidator(10), MaxValueValidator(50)])
    url_sub = models.CharField(default='v02', max_length=30)
    jpeg_quality_sub = models.IntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(80)])
    gop_sub = models.IntegerField(default=30, validators=[MinValueValidator(1), MaxValueValidator(90)])
    resolution_width_sub = models.IntegerField(default=960)
    resolution_height_sub = models.IntegerField(default=720)
    frame_rate_sub = models.IntegerField(default=30, validators=[MinValueValidator(1), MaxValueValidator(30)])
    video_encoding_sub = models.IntegerField(default=VideoEncodingChoices.CBR, choices=VideoEncodingChoices.choices)
    
    # thirdtream
    enabled_third = models.BooleanField(default=True)
    encode_type_third = models.IntegerField(default=EncodeTypeChoices.MJPEG, choices=EncodeTypeChoices.choices)
    bit_rate_third = models.IntegerField(default=1500, validators=[MinValueValidator(256), MaxValueValidator(2048)])
    quality_third = models.IntegerField(default=40, validators=[MinValueValidator(10), MaxValueValidator(50)])
    url_third = models.CharField(default='v03', max_length=30)
    jpeg_quality_third = models.IntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(80)])
    gop_third = models.IntegerField(default=30, validators=[MinValueValidator(1), MaxValueValidator(90)])
    resolution_width_third = models.IntegerField(default=1280)
    resolution_height_third = models.IntegerField(default=960)
    frame_rate_third = models.IntegerField(default=15, validators=[MinValueValidator(1), MaxValueValidator(15)])
    video_encoding_third = models.IntegerField(default=VideoEncodingChoices.CBR, choices=VideoEncodingChoices.choices)
    
    @staticmethod
    def get_resulution_options(encode_type: int = 0) -> List[Tuple[int, int]]:
        resolution_options = [
            [(2592, 1944), (2048, 1536), (1600, 1200), (1280, 960)],
            [(960, 720), (704, 576), (640, 480)],
            [(960, 720), (704, 576), (640, 480)]
        ]
        
        return resolution_options[encode_type]
    
    
class DeviceImageInfo(models.Model):
    class ICRChoices(models.IntegerChoices):
        Auto = 0
        Night = 1
        Day = 2
        Schedule = 3
    
    class BWModeChoices(models.IntegerChoices):
        By_IR_type = 0
        BW = 1
        Color = 2
        
    class WBChoices(models.IntegerChoices):
        ATW = 0
        Incandescent_light = 1
        Cool_light = 2
        Sun_light = 3
        Cloudy = 4
        Sun_shady = 5
    
    class FlicknessChoices(models.IntegerChoices):
        Auto = 0
        flicker_free_50hz = 1
        flicker_free_60hz = 2
        
    class DayModeExposureChoices(models.IntegerChoices):
        Auto = 0
        Manual = 1
    
    class NightModeExposureChoices(models.IntegerChoices):
        Auto = 0
        Manual = 1
        Off = 2
    
    # Mirror/flip
    flip = models.BooleanField(default=False)
    mirror = models.BooleanField(default=False)
    
    # ICR
    icr = models.IntegerField(default=ICRChoices.Auto, choices=ICRChoices.choices)
    icr_day_mode_start = models.TimeField(default=datetime.time(6, 0))
    icr_day_mode_end = models.TimeField(default=datetime.time(18, 0))
    
    # B/W
    bw_mode = models.IntegerField(default=BWModeChoices.By_IR_type, choices=BWModeChoices.choices)
    
    # WB
    wb_enabled = models.BooleanField(default=True)
    wb_scene_mode = models.IntegerField(default=WBChoices.ATW, choices=WBChoices.choices)
    wb_scene_value = models.IntegerField(default=0)
    
    # Exposure
    exposure_enabled = models.BooleanField(default=True)
    flickness = models.IntegerField(default=FlicknessChoices.Auto, choices=FlicknessChoices.choices)
    day_mode_exposure = models.IntegerField(default=DayModeExposureChoices.Auto, choices=DayModeExposureChoices.choices)
    day_exposure_time = models.IntegerField(default=30, validators=[MinValueValidator(30), MaxValueValidator(10000)])
    day_exposure_gain = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(16)])
    night_mode_exposure_enabled = models.BooleanField(default=False)
    night_mode_exposure = models.IntegerField(default=NightModeExposureChoices.Off, choices=NightModeExposureChoices.choices)
    night_exposure_time = models.IntegerField(default=30)
    night_exposure_gain = models.IntegerField(default=15, validators=[MinValueValidator(1), MaxValueValidator(15)])
    
    # Image Enhancement
    # Day Mode
    brightness = models.IntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(100)])
    sharpness = models.IntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(100)])
    contrast = models.IntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(100)])
    hue = models.IntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(100)])
    saturation = models.IntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(100)])
    wdr_enabled = models.BooleanField(default=False)
    wdr = models.IntegerField(null=True, default=None, validators=[MinValueValidator(1), MaxValueValidator(10)])
    # Night Mode
    brightness_night = models.IntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(100)])
    sharpness_night = models.IntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(100)])
    contrast_night = models.IntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(100)])
    hue_night = models.IntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(100)])
    saturation_night = models.IntegerField(default=50, validators=[MinValueValidator(1), MaxValueValidator(100)])
    wdr_night_enabled = models.BooleanField(default=False)
    wdr_night = models.IntegerField(null=True, default=None, validators=[MinValueValidator(1), MaxValueValidator(10)])
    
    # Defog
    defog = models.BooleanField(default=False)
    
    
class DeviceNetworkInfo(models.Model):
    class RTSPAuthChoices(models.IntegerChoices):
        Anonymous = 0
        Authentication = 1
    
    # IPv4
    static_ip_address = models.CharField(null=True, default=None, max_length=30)
    dhcp_ip_address = models.CharField(null=True, default=None, max_length=30)
    netmask = models.CharField(null=True, default=None, max_length=30)
    gateway = models.CharField(null=True, default=None, max_length=30)

    # DNS
    dns_primary = models.CharField(null=True, default=None, max_length=30)
    dns_secondary = models.CharField(null=True, default=None, max_length=30)
    
    # NTP
    # server setting
    ntp_address = models.CharField(null=True, default=None, max_length=30)
    from_dhcp = models.BooleanField(null=True, default=None)
    update_per_minutes = models.IntegerField(default=10)
    # port
    enable_http = models.BooleanField(default=True)
    http_port = models.IntegerField(default=80)
    enable_rtsp = models.BooleanField(default=True)
    rtsp = models.IntegerField(default=554)
    enable_ftp = models.BooleanField(default=True)
    ftp = models.IntegerField(default=21)
    enable_upnp = models.BooleanField(default=True)
    enable_arp_ping = models.BooleanField(default=True)
    
    # RTSP setting
    rtsp_auth = models.IntegerField(default=RTSPAuthChoices.Anonymous, choices=RTSPAuthChoices.choices)
    rtsp_auth_username = models.CharField(null=True, default=None, max_length=30)
    rtsp_auth_password = models.CharField(null=True, default=None, max_length=30)


class DeviceInfo(models.Model):
    basic_info = models.ForeignKey(DeviceBasicInfo, on_delete=models.CASCADE)
    network_info = models.ForeignKey(DeviceNetworkInfo, on_delete=models.CASCADE)
    video_info = models.ForeignKey(DeviceVideoInfo, on_delete=models.CASCADE)
    image_info = models.ForeignKey(DeviceImageInfo, on_delete=models.CASCADE)
