__author__ = 'TYM'
import re

class JsCompressor:
    def _remove_blanks(func):
        def __decorator(s):
            s = func(s)
            return ''.join(map(lambda l: l.strip(), s.split('\n')))
        return __decorator

    def _remove_single_line_comments(func):
        def __decorator(s):
            s = func(s)
            single_line_comment_pattern = re.compile(r'//[^\n]*?\n')  # non-greedy mode
            s = re.sub(single_line_comment_pattern, '', s)
            return s
        return __decorator

    def _remove_multi_line_comments(func):
        def __decorator(s):
            s = func(s)
            multi_line_comment_pattern = re.compile(r'/\*[\s\S]*?\*/')  # non-greedy mode
            s = re.sub(multi_line_comment_pattern, '', s)
            return s
        return __decorator

    @_remove_blanks
    @_remove_multi_line_comments
    @_remove_single_line_comments
    def compress(s):
        return s


class PhpCompressor:
    def _remove_blanks(func):
        def __decorator(s):
            s = func(s)
            return ''.join(map(lambda l: l.strip(), s.split('\n')))
        return __decorator

    def _remove_single_line_comments(func):
        def __decorator(s):
            s = func(s)
            single_line_comment_pattern = re.compile(r'//[^\n]*?\n')  # non-greedy mode
            s = re.sub(single_line_comment_pattern, '', s)
            single_line_comment_pattern = re.compile(r'#[^\n]*?\n')  # non-greedy mode
            s = re.sub(single_line_comment_pattern, '', s)
            return s
        return __decorator

    def _remove_multi_line_comments(func):
        def __decorator(s):
            s = func(s)
            multi_line_comment_pattern = re.compile(r'/\*[\s\S]*?\*/')  # non-greedy mode
            s = re.sub(multi_line_comment_pattern, '', s)
            return s
        return __decorator

    @_remove_blanks
    @_remove_multi_line_comments
    @_remove_single_line_comments
    def compress(s):
        return s
