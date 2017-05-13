# Liferea Plugins #
An ambitiously named collection of a single plugin.

## To install ##
There is only one plugin at present, but it has its own directory. If I add any other plugins, they will also each have their own directory.

To install a plugin, copy the contents of the desired plugin directory to:
`~/.local/share/liferea/plugins`

The plugin can be activated in Liferea from the `Tools -> Preferences -> Plugins` menu.

## Feedalerts ##
At present, this can only be configured by directly editing the feedalerts.conf file. There is only one section (Main) and one key (Search). An empty search string will match everything, otherwise you can use any Python regular expression to match the feed title.
