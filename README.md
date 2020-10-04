# subtitle-sequences-sync
This script will get a SRT subtitle file in input and will output a new SRT file with synced timings when timings are the same for multiple sequences.

## Example

```
8
00:00:24,543 --> 00:00:26,752
<i>♪ For what</i>

9
00:00:24,543 --> 00:00:26,752
<i>I've been missing ♪</i>
```

will become

```
8
00:00:24,543 --> 00:00:26,752
<i>♪ For what</i>
<i>I've been missing ♪</i>
```
