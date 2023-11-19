from django import forms
from .models import ChannelsForm , ChannelVideo , Shorts


class ChannelDetailsForm(forms.ModelForm):
    class Meta:
        model = ChannelsForm
        fields = ['title','desc','content','channelimages','channelthumbles']

class VideoDetailsForm(forms.ModelForm):
    class Meta:
        model =  ChannelVideo
        fields = ['videotitle','videodesc','channelimages','channelthumbles','smallimage','channelname']


class ChannelShorts(forms.ModelForm):
    class Meta:
        model =  Shorts
        fields = ['shortchannelname','shortvideo']



