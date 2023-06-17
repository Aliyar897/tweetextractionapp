"""
URL configuration for tweetextraction project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mytweetapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.extractTweet,  )
]




#   auth = tweepy.OAuth1UserHandler(
#     "ej2IjtCX4VRPSb282fvUj0Tz4", "twsxDdlYy3YNbz13d6XpgulPtON5u2QuoyeDTv4ELpTc8FEEqn",
#     "1667028061190246401-kWrVSdL0qhWVkthNYtp2jjTG2WBP32", "VAW1mbG4nm2vyUs46AcYkyTslhS1UiAiqHHXdmsdbAHkd"
#     ) twiter api of mine


    # auth = tweepy.OAuth1UserHandler(
    # "eGNFR0dBeFZ4eXZud1hGMUhJM006MTpjaQ", "_8-mPChiJHGBUbmO5-J7Flm4ZPSHzGvwB2vDHsblFmWIJcYoz8",
   #client id and token 