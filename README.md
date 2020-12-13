# cathacks-2020
This is the repository for all of my work on the University of Kentucky CatHacks event.

## weatherbuddy
Weatherbuddy is a tool that exists to dynamically change the colorscheme of your environment to match the current weather.

Utilizing py-wal and the united states weather.gov api, it finds the current time and updates your environment to a colorscheme decided by you. 

It has basic extensabiity through configuration but for changing the theme decision logic it would be best to hack some stuff in by hand at current time.

## Known bugs at this time

Only attempts to update Xresourses and i3, as using `pywal.reload.env()` also reloads polybar, which causes large and disruptive geometry glitches on my system, and as such is not usable, I may move away from polybar for this reason, but do not yet have a good alternative.

Forecast caching is completely busted, I am currently calling this script with the `--returnCurrent` flag as a custom polybar script, however I would prefer to instead have it run as a `systemd --user` daemon. Getting this configuration to work feels out of scope for this hackathon however. 

## Possible improvements to be made

- Fix the cache to reduce load on web server
- Add respect for the hourly forecast
- Override themes based on tempature vs percipitation (e.g. always use the "rain" theme no matter the temperature)


