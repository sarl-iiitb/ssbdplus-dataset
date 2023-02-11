## SSBDPLUS Dataset

A sample file is given as follows:
```xml
<?xml version="1.0" encoding="utf-8"?>
<video id="action_3">
   <url>https://www.youtube.com/watch?v=AbieKDKqkto</url>
   <behaviours count="1">
      <behaviour id="b_01">		
         <time>6:10</time>		
         <category>armflapping</category>		
      </behaviour>
   </behaviours>
</video>
```  

The key points to note are as follows:
- The `url` key contains the YouTube URL of the video containing `count` actions - as of Feb 7 2023, all videos are up and accessible.
- The `time` field corresponding to each behaviour has the following format: `(start_time_in_seconds):(end_time_in_seconds)`. So, in this example, [this video](https://www.youtube.com/watch?v=AbieKDKqkto) has an `armflapping` behaviour from 6 to 10 seconds from the start of the video.

## Parser

Researchers may use the [parser tool](../parser/parse.py) provided with this repository to extract and use features from the XML files. All documentation pertaining to the return type of the parser has been provided in the same.