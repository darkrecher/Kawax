# Extrait d'un message de forum à propos de pygame to exe


## Méta-données

Url originale :
https://www.daniweb.com/programming/software-development/threads/247249/need-help-with-pygame-to-exe#post1081038

Date de récupération :
2015-12-15

Sujet du topic :
Need help with pygame to exe

3 Contributors
5 Replies
7 Views
1 Year Discussion Span
4 Years Ago

tag :
python

## Question

So i made a small game using pygame, and I want to be able to give it out to some friends who don't have python, so I want to make it into an EXE. i've been trying for several hours using several different methods, but nothings seems to be working. I would REALLY appreciate any help.

So after all this time I think py2exe appears to be the best tool to use. I have it installed, I just can't get it to work correctly on my game. After looking for many different setup.py file thingys, this is the one i've been using most recently:

    try:
        from distutils.core import setup
        import py2exe, pygame
        from modulefinder import Module
        import glob, fnmatch
        import sys, os, shutil
    except ImportError, message:
        raise SystemExit,  "Unable to load module. %s" % message

    class pygame2exe(py2exe.build_exe.py2exe): #This hack make sure that pygame default font is copied: no need to modify code for specifying default font
        def copy_extensions(self, extensions):
            #Get pygame default font
            pygamedir = os.path.split(pygame.base.__file__)[0]
            pygame_default_font = os.path.join(pygamedir, pygame.font.get_default_font())

            #Add font to list of extension to be copied
            extensions.append(Module("pygame.font", pygame_default_font))
            py2exe.build_exe.py2exe.copy_extensions(self, extensions)

    class BuildExe:
        def __init__(self):
            #Name of starting .py
            self.script = "game.py"

            #Name of program
            self.project_name = "MyApps"

            #Project url
            self.project_url = "about:none"

            #Version of program
            self.project_version = "0.0"

            #License of the program
            self.license = "MyApps License"

            #Auhor of program
            self.author_name = "Me"
            self.author_email = "example@example.com"
            self.copyright = "Copyright (c) 2009 Me."

            #Description
            self.project_description = "MyApps Description"

            #Icon file (None will use pygame default icon)
            self.icon_file = None

            #Extra files/dirs copied to game
            self.extra_datas = ['background.mid','background.png','bonus.png','cowbell.wav','highscore.txt']

            #Extra/excludes python modules
            self.extra_modules = []
            self.exclude_modules = []

            #DLL Excludes
            self.exclude_dll = ['']

            #Zip file name (None will bundle files in exe instead of zip file)
            self.zipfile_name = None

            #Dist directory
            self.dist_dir ='dist'

        ## Code from DistUtils tutorial at http://wiki.python.org/moin/Distutils/Tutorial
        ## Originally borrowed from wxPython's setup and config files
        def opj(self, *args):
            path = os.path.join(*args)
            return os.path.normpath(path)

        def find_data_files(self, srcdir, *wildcards, **kw):
            # get a list of all files under the srcdir matching wildcards,
            # returned in a format to be used for install_data
            def walk_helper(arg, dirname, files):
                if '.svn' in dirname:
                    return
                names = []
                lst, wildcards = arg
                for wc in wildcards:
                    wc_name = self.opj(dirname, wc)
                    for f in files:
                        filename = self.opj(dirname, f)

                        if fnmatch.fnmatch(filename, wc_name) and not os.path.isdir(filename):
                            names.append(filename)
                if names:
                    lst.append( (dirname, names ) )

            file_list = []
            recursive = kw.get('recursive', True)
            if recursive:
                os.path.walk(srcdir, walk_helper, (file_list, wildcards))
            else:
                walk_helper((file_list, wildcards),
                            srcdir,
                            [os.path.basename(f) for f in glob.glob(self.opj(srcdir, '*'))])
            return file_list

        def run(self):
            if os.path.isdir(self.dist_dir): #Erase previous destination dir
                shutil.rmtree(self.dist_dir)

            #Use the default pygame icon, if none given
            if self.icon_file == None:
                path = os.path.split(pygame.__file__)[0]
                self.icon_file = os.path.join(path, 'pygame.ico')

            #List all data files to add
            extra_datas = []
            for data in self.extra_datas:
                if os.path.isdir(data):
                    extra_datas.extend(self.find_data_files(data, '*'))
                else:
                    extra_datas.append(('.', [data]))

            setup(
                cmdclass = {'py2exe': pygame2exe},
                version = self.project_version,
                description = self.project_description,
                name = self.project_name,
                url = self.project_url,
                author = self.author_name,
                author_email = self.author_email,
                license = self.license,

                # targets to build
                windows = [{
                    'script': self.script,
                    'icon_resources': [(0, self.icon_file)],
                    'copyright': self.copyright
                }],
                options = {'py2exe': {'optimize': 2, 'bundle_files': 1, 'compressed': True, \
                                      'excludes': self.exclude_modules, 'packages': self.extra_modules, \
                                      'dll_excludes': self.exclude_dll} },
                zipfile = self.zipfile_name,
                data_files = extra_datas,
                dist_dir = self.dist_dir
                )

            if os.path.isdir('build'): #Clean up build dir
                shutil.rmtree('build')

    if __name__ == '__main__':
    	if len(sys.argv):
    		sys.argv.append('py2exe')
        	BuildExe().run()
        	raw_input("Press any key to continue") #Pause to let user see that things ends

When I try this however, I get the error:
NotImplementedError: font module not available
(ImportError: MemoryLoadLibrary failed loading pygame\font.pyd)

In my actual code, I'm loading font using:
font = pygame.font.SysFont("freesansbold", 48)

as I heard this is the better way to do it.

I've tried many different setup.py files, but each gives me a different error, whether it be missing DLL's, or font, or something else. If I could get any help with this, i would appreciate it.

*Author : sinisterduke*
*5 posts since Dec 2009*

## Réponse 01

Just a small update:

I went through my code and removed all instances of font. Now I get this:

(ImportError: MemoryLoadLibrary failed loading pygame\mixer.pyd)

*Author : sinisterduke*

*5 Years Ago*

## Réponse 02

and I went through and removed every instance of using sounds/mixer, and now it works. The problem is, I kinda need text and sound. If anyone has any suggestions, I'd appreciate it. It's probably just something small or stupid

*Author : sinisterduke*

*5 Years Ago*

## Réponse 03

Pygame and py2exe don't get along well, you have to do a few things to get it working. Take a look: http://www.moviepartners.com/blog/2009/03/20/making-py2exe-play-nice-with-pygame/

A great idea is to make a list of the modules you need.

*Author : ov3rcl0ck*

*5 Years Ago*

## Réponse 04

I've tried that site and everything it suggests already, but it hasn't worked.

*Author : sinisterduke*

*5 Years Ago*

## Réponse 05

I realize this's and older thread and is being addressed a few other places, but since it is the result that came up when i googled the exact error message i received, please consider the following: To the best of my knowledge, pygame2exe only works with a slightly older version of python/pygame libraries. I've banged into the exact same brick walls as sinisterduke here, until i uninstalled python 2.6 and reloaded with the following, which are still available somewhere on the respective product's sites.

python-2.5.4.msi
pygame-1.9.1.win32-py2.5.msi
py2exe-0.6.9.win32-py2.5.exe

Good Luck!

*Author : tendragons*

*4 Years Ago*
