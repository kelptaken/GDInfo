# GDInfo
Geometry Dash swiss knife

## But what can it do?
1. check full info about a level
2. check full info about an account (including unique Player ID)
3. export to JSON
4. download user's icons to PNG

## 2.0 is out!
I wanted to add lists (comments, post, comment history, level searching), but realised it is impossible and unfortunately, it will never be added in GDInfo. :(

1. Level info now shows a lot of additional info. (it is now 2x slower, but 2x more info!) (there are even more info listed in the API, such as the level data, but level downloading has been disabled by RobTop.)
- Shows how much stars, orbs and diamonds you get for beating the level.
- Shows the game version the level was released/updated in.
- If the level is an Extreme Demon, shows demonlist position.
- Shows how much coins are in the level and are they verified.
- Shows the song size and raw link to directly song's MP3 file.
- Shows is the level large (more than 40,000 objects)
2. Menu is now structured and divided to 3 steps.
3. Now there are only 2 modules for level and account operations, new features are added as new functions in modules.
4. Fixed the bug with official songs (issue #1)

## Bugs
Wow, you found it? Issues tab is for you!

## Under the hood
GDInfo is using GDBrowser.com's API

## TO-DO
1. Implement lists (posts, comments, search) and additional input (to make actions more structured)
