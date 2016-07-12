# youtube-populator

## Summary

youtube-populator is a script you can use to download
youtube videos and save it in a form that kodi finds them as series.

You can use it together with flexget to add rss-streams.

Was inspired by Kaimis Blogpost here:
<http://kaimi.cc/2014/09/16/youtube-im-offline-modus/>

just wasnt good enough for me :)


## Howto use

  * install/setup flexget

  * install youtube-dl

  * pull/download this python script


  * add following lines under Template:
  
```
  youtube-filtered:
    exec:
      on_output:
        for_accepted:
          - <<PATH TO SCRIPT>>/youtube-populator.py "{{url}}" &
  youtube:
    accept_all: yes
    template: youtube-filtered
```
dont forget to replace the PATH TO SCPIPT code.


  * add for each stream you want to watch something like that:
```
  yt_Sacha-Chua:
    rss: https://www.youtube.com/feeds/videos.xml?channel_id=UClT2UAbC6j7TqOWurVhkuHQ
    template: youtube
```

  * Done!


## Contributing

Yes, please do! See [CONTRIBUTING][] for guidelines.

## License

See [COPYING][]. Copyright (c) 2016 Stefan Huchler.


[CONTRIBUTING]: ./CONTRIBUTING.md
[COPYING]: ./COPYING
