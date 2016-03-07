from django.conf.urls import include, patterns, url

from .api_resources import FacilityResource, FacilityGroupResource, FacilityUserResource, SummaryLogResource, VideoLogResource, AudioLogResource, PDFLogResource

urlpatterns = patterns(__package__ + '.api_views',
    url(r'^', include(FacilityResource().urls)),
    url(r'^', include(FacilityGroupResource().urls)),
    url(r'^', include(FacilityUserResource().urls)),
    url(r'^', include(SummaryLogResource().urls)),
    url(r'^', include(VideoLogResource().urls)),
    url(r'^', include(AudioLogResource().urls)),
    url(r'^', include(PDFLogResource().urls)),
)