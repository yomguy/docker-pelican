# docker-pelican

docker composition for [Pelican](https://github.com/getpelican/pelican-plugins) based web sites with webhook auto builder

# Install

```
git clone --recursive https://github.com/yomguy/docker-pelican.git`
```

This will also checkout all pelican plugins. To get all pelican-themes:

```
cd lib/pelican-themes
git submodule update
```

# Configure

The config file is `app/pelicanconf.py`

# Get text sources

You will need a separate repository for your text sources. Clone it in the var/in directory, for example:

```
cd var
git clone https://github.com/yomguy/musichacking2017.git
```

# Start

```
docker-compose up
```

# Trigger

The app can automatically be triggered by a webhook as explained [here](https://github.com/yomguy/pelicangit)

# Enjoy!
