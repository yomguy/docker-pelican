# docker-pelican

docker composition for static [Pelican](https://github.com/getpelican/pelican-plugins) based web sites with webhook auto builder

# Install

```
git clone --recursive https://github.com/yomguy/docker-pelican.git`
```

This will also checkout all pelican plugins.

To get all pelican-themes, just do:

```
cd lib/pelican-themes
git submodule update
```

# Configure

The config file is `app/pelicanconf.py`

# Feed

You will need a separate repository for your input text sources.

Clone your repo in the `var/in` directory, for example:

```
git clone https://github.com/yomguy/musichacking2017.git var/in
```

# Start

```
docker-compose up
```

# Trigger

The app can automatically be triggered by a webhook as explained [here](https://github.com/yomguy/pelicangit)

The default port in 8888 in our case.

# Enjoy!

with love <3

# License

docker-pelican is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

mezzanine-organization is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

Read the LICENSE.txt file for more details.
