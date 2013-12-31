import utils

utils.initialize_build()
name = "my_video_plugin"
out_path = utils.create_bin_name(name)

env = Environment(CPPPATH=[
                    '/usr/include/vlc',
                    '/usr/include/vlc/plugins',
                    'include'],
                  CFLAGS=[
                    '-std=gnu99',
                    '-g',
                    '-Wall',
                    '-Wextra',
                    '-O2',
                    '-DPIC'
                  ],
                  LIBPATH=[
                    '/usr/lib/',
                    '/usr/local/lib'],
                  LIBS=[
                    'libvlc'])

env.MergeFlags('!pkg-config --cflags vlc-plugin')
env.MergeFlags('!pkg-config --libs vlc-plugin')
env.MergeFlags('-Wl,-no-undefined,-z,defs')

#Alias install to put the .so library where it needs to be for VLC to use it
env.Alias('install', ['/usr/lib/vlc/plugins/video_output'])

#Collect all the source files
src_files = utils.get_source_list(base = "src", recursive = True)

#Create the Shared Object Library
sl = env.SharedLibrary(target = out_path, source = src_files)

#Install the library
env.Install(dir = "/usr/lib/vlc/plugins/video_output", source = sl)

