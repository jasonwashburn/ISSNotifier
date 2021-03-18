# ISS Notifier

               __
     ________ /==\ _________
    |=|==|==|-|  |-|==|==|==|
    |=|=ISS=|-|  |-|=ISS=|==|
    ^"""""""" \==/ """""""""^
               ||  |=|=|=|  .
        }:{    !!  |=|=|=| /
     *)-[[[[[[(OO)]]]]]]]]X-(~
        }:{    ||  |=|=|=| \
               ||  |=|=|=|  '
               !!
     ________ /==\ _________
    |=|==|==|-|  |-|==|==|==|
    |=|=ISS=|-|  |-|=ISS=|==|
    ^"""""""" \==/ """""""""^
               ++


A python script that uses the gmail smtp server to automatically notify you when the International Space Station is 
overhead (within 5 degrees latitude or longitude) and it's dark (between the ending and beginning of astrological 
twilight)

Uses:
The sunrise-sunset.org API. [Documentation](https://sunrise-sunset.org/api)
The open-notify ISS-Location-Now API. [Documentation](http://open-notify.org/Open-Notify-API/ISS-Location-Now/)

**To Use**: 
1. Install the required packages in `requirements.txt`.
2. Rename the `example_config.py` to `config.py` and enter your gmail credentials and name for the email closing.

*Note: In order for this to work, you must enable less secure apps for your Google account. For this reason, I **strongly** recommend using a new gmail
account rather than your main.*

[Enabling Less Secure Access in Gmail](https://bytexd.com/less-secure-apps-gmail/)