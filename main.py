__author__ = 'TYM'
import os
import logging
import compressor
import config

# 将目录下的所有以extension为扩展名的文件，用compress处理并写到对应目录中
def dispatch(extension, compress):
    for s_root, dirs, files in os.walk(config.SOURCE_DIR):
        if files:
            t_root = s_root.replace(config.SOURCE_DIR, config.TARGET_DIR)
            # os.chdir(t_root)
            for file in files:
                if file.split('.')[-1].lower() == extension.lower():
                    with open('%s/%s' % (s_root, file), 'r', encoding=config.SOURCE_ENCODING) as fin:
                        with open('%s/%s' % (t_root, file), 'w', encoding=config.TARGET_ENCODING) as fout:
                            fout.write(compress(fin.read()))

if __name__ == '__main__':
    if os.path.exists(config.TARGET_DIR):
        logging.error('target dir already exists.')
        raise(SystemExit)
    else:
        os.mkdir(config.TARGET_DIR)

    # copy dir structure
    for root, dirs, files in os.walk(config.SOURCE_DIR):
        if dirs:
            root = root.replace(config.SOURCE_DIR, config.TARGET_DIR)
            os.chdir(root)
            for dir in dirs:
                os.mkdir(dir)

    compressor_map = {
        'javascript': compressor.JsCompressor,
        'php': compressor.PhpCompressor
    }

    for key in config.EXTENSION:
        if key in compressor_map:
            if type(config.EXTENSION[key]) == type(''):
                dispatch(config.EXTENSION[key], compressor_map[key].compress)
            elif type(config.EXTENSION[key]) == type([]):
                for ext in config.EXTENSION[key]:
                    dispatch(ext, compressor_map[key].compress)
        else:
            logging.warning('%s compressor not found.' % key)
