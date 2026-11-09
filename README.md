# newstatunlocked-studio

Automated studio for the New Stat Unlocked YouTube Shorts channel. A daily Claude scheduled task picks an idea, writes the script, voices it (Kokoro, open source), animates it with the engine in `engine/`, commits the video to `videos/`, and publishes two Shorts a day (YouTube + Facebook) through Zernio. Every script gets one independent critic pass (CRITIC.md) before it's animated.

- `PIPELINE.md`: the daily run
- `WRITING.md`: channel bible and script rules
- `engine/`: render engine, voice tool, style guide
- `episodes.json`: every episode and its status
- `episodes/epNN/`: script, scene plan, upload pack and thumbnail for each episode
- `videos/`: rendered Shorts (deleted 7 days after posting)
