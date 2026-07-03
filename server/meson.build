project('targets', 'c',
    meson_version: '>= 0.55.0',
    default_options: [
        'b_asneeded=false',
        'b_colorout=never',
        'b_pch=false',
        'b_staticpic=false',
    ]
)

incdir = include_directories('inc')

sources = files(
    'src/micro_dp.c',
    'src/micro_dp_0x00.c',
    'src/micro_dp_0x01.c',
    'src/micro_dp_0x02.c',
    'src/micro_dp_0x03.c',
    'src/micro_dp_0x04.c',
    'src/micro_dp_crc16.c',
)

optimization = meson.get_external_property('optimization')
fpu = meson.get_external_property('fpu')
float_abi = meson.get_external_property('float_abi')
compiler = meson.get_external_property('compiler')
name = meson.get_external_property('name')

found_compiler = find_program(compiler, required: false)

if not found_compiler.found()
    error('Compiler' + compiler + ' not found!')
endif

suffix = '_' + optimization

if optimization == 'size'
    if compiler == 'c28x'
        optim_flag = ['--opt_for_speed=0']
    else
        optim_flag = ['-Os']
    endif
else
    if compiler == 'clang'
        optim_flag = ['-O3', '-ffast-math']
    elif compiler == 'gcc'
        optim_flag = ['-Ofast']
    elif compiler == 'c28x'
        optim_flag = ['--opt_for_speed=5']
    else
        optim_flag = []
    endif
endif

cpu = host_machine.cpu()

if cpu == 'c28x'
    cc = meson.get_compiler('c')
    cc_cmd = cc.cmd_array()[0]
    cc_prog = find_program(cc_cmd, required: true)
    
    fs = import('fs')
    cc_include_dir = fs.parent(fs.parent(cc_prog.full_path())) / 'include'

    c_args = [
        '-v28',
        '-ml',
        '-mt',
        '-O4',
        '--symdebug:none',
        '--c11',
        '--abi=eabi',
        '--include_path=' + cc_include_dir,
    ]

elif cpu == 'rv32i'
    c_args = [
        '-march=rv32imc',
        '-mabi=ilp32',
        '-std=c11',
        '-mcmodel=medlow',
        '-fsigned-char',
        '-ffunction-sections',
    ]

elif cpu == 'x86_64'
    c_args = [
        '-DMICRO_DP_EXPORTS'
    ]

    shared_library(
        name + suffix, 
        sources,
        include_directories : incdir,
        c_args: c_args,
        install : true
    )

    subdir_done()

else
    c_args = [
        '-std=c11',
        '-mcpu=' + cpu,
        '-ffunction-sections',
        '-fdata-sections',
        '-fno-strict-aliasing',
        '-fno-rtti',
        '-mlittle-endian',
        '-fshort-wchar',
        '-fshort-enums',
        '-mthumb',
    ]

    if compiler == 'clang'
        c_args += ['--target=arm-none-eabi']
    elif compiler == 'gcc'
        c_args += ['--specs=nano.specs']
    endif

    c_args += [
        '-mfpu=' + fpu,
        '-mfloat-abi=' + float_abi,
    ]
endif

c_args += optim_flag

static_library(
    name + suffix,
    sources,
    include_directories: incdir,
    c_args: c_args,
    install: true,
)