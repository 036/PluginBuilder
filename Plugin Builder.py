import os

#Store the core file requirements in original var
original = '''<?php

/**
 *  %name% Core Plugin File
 *
 *  %description%
 *
 * @package %name%
 * @author  %author%
 * @version 1.0.0
 */

// Disallow direct access to this file for security reasons
if(!defined("IN_MYBB"))
{
	die("Direct initialization of this file is not allowed.");
}

$plugins->add_hook( 'hook_name','hook_function');

function %plugin-name%_info()
{
	return array(
		"name"			=> "%name%",
		"description"	=> "%description%",
		"website"		=> "%website%",
		"author"		=> "%author%",
		"version"		=> "1.0",
		"compatibility" => "*"
	);
}

function %plugin-name%_install()
{
	global $db;
}

function %plugin-name%_is_installed()
{
	global $db;
}

function %plugin-name%_uninstall()
{
	global $db;
}

function %plugin-name%_activate()
{
	global $db;
}

function %plugin-name%_deactivate()
{
	global $db;
}
'''

logo = input("""\
 Press Enter to Start

""")

#Grab the user input
author = input("Author Name: ")
name = input("Info Plugin Name: ")
website = input("Website: ")
plugin = input("Plugin name(used on functions): ")
description = input("Plugin Description: ")

#Replace the content with the user input
original = original.replace("%author%",author)
original = original.replace("%name%",name)
original = original.replace("%website%",website)
original = original.replace("%plugin-name%",plugin)
original = original.replace("%description%",description)

#If inc directory does not exist create directory
if not os.path.exists("inc"):
	os.makedirs("inc")
#If plugins directory does not exist create directory
if not os.path.exists("inc/plugins"):
	os.makedirs("inc/plugins")
#Create the file name inside inc/plugins/ from the user input
f = open("inc/plugins/" + plugin + ".php","w")
#Write the updated original var to the file
f.write(original)
f.close()
