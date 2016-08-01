import os

original = '''<?php

/**
 *  %name% Core Plugin File
 *
 *  %description%
 *
 * @package %name%
 * @author  Paradigm
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
		"author"		=> "Paradigm",
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


name = input("Info Plugin Name: ")
website = input("Website: ")
plugin = input("Plugin name(used on functions): ")
description = input("Plugin Description: ")

original = original.replace("%name%",name)
original = original.replace("%website%",website)
original = original.replace("%plugin-name%",plugin)
original = original.replace("%description%",description)


if not os.path.exists("inc"):
	os.makedirs("inc")
if not os.path.exists("inc/plugins"):
	os.makedirs("inc/plugins")

f = open("inc/plugins/" + plugin + ".php","w")
f.write(original)
f.close()
 
