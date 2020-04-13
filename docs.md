# Things to know when using this with the API

There are formats that are not consistent with all attributes.

- Values in `videoCodec` and `audioCodec` contain version-information. These are not consistent with itags.
- The following sets of `videoCodec` occur but are interchangeable:
  - `AVC...` == `H.264...`
- The following sets of `audioCodec` occur but are interchangeable:
  - `AAC...` == `MP4A...`
- The following sets of `container` occur but are interchangeable:
  - `mp4` == `m4a`
- **Every** format occurs with and without `quality`. This includes audio-only formats.
- **Every** audio-only format occurs with and without `audioQuality`, `audioBitrate` and `audioSampleRate`.

# Known inconsistencies

- itag `18` occurs with the following value-combinations of `qualityLabel/quality`: `144p/small`, `240p/tiny` and `360p/medium`. `360p/medium` should be the case for all videos where the source-file has a resolution of at least `360p`.
- itag `133` occurs with the following value-combinations of `qualityLabel/quality`: `144p/small`, `240p/tiny`. `240p/tiny` should be the case for all videos where the source-file has a resolution  of at least `240p`.
- itag `242` occurs with the following value-combinations of `qualityLabel/quality`: `144p/small`, `240p/tiny`. `240p/tiny` should be the case for all videos where the source-file has a resolution  of at least `240p`.
- itag `271` occurs with the following values of `qualityLabel`: `1080p`, `1440p`
- itag `272` occurs with the following values of `qualityLabel`: `4320p`, `4320p50`, `4320p60`
- itag `278` occurs with the following values of `qualityLabel`: `144p`, `144p 15fps`. However, its seems that videos with `144p 15fps` have 30 fps too.
- itag `398` occurs with the following values of `qualityLabel`: `720p`, `720p60`
- itag `399` occurs with the following values of `qualityLabel`: `1080p`, `1080p60`
- Most HFR-formats occur with values of `qualityLabel` suffixing either `50` or `60`. This includes itags `272`, `298`, `299`, `302`, `303`, `308`, `315`, `398`, `399`.

**The yt-itag datasets list the best possible format for every itag.**

# Problematic formats

- Formats with itags `300` or `301` doesn't contain any information when queried via the API. However the files can be inspected when downloaded. They only seem to occur on some ended livestreams.
- Formats with itags `386` or `387` doesn't contain any information when queried via the API. Not even a codec. These files can not be downloaded. They only seem to occur on some running livestreams.

# Other observations

- It seems that all videos are available in formats with itags `18`, `133`, `140`, `160`, `242`, `251` and `278`.
- It seems that all videos >= 360p are available in formats with itags `134`, `135`, `243`, `244`, `249` and `250`.
