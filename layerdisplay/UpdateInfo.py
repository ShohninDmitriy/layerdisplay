def get_update_information(plugin):
		return dict(
			layerdisplay=dict(
				displayName=plugin._plugin_name,
				displayVersion=plugin._plugin_version,

				type="github_release",
				current=plugin._plugin_version,
				user="ShohninDmitriy",
				repo="LayerDisplay",

				pip="https://github.com/ShohninDmitriy/layerdisplay/archive/{target_version}.zip"
			)
		)
