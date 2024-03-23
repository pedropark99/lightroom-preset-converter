from typing import (
    Union,
    Optional,
    Dict,
    List
)
import re
import json

TEMPLATE_KEY_REGEX = r'(?P<spaces>\s*)(?P<key>[A-Za-z0-9]+) = '
is_not_blank = lambda x: x != "" and not re.search(r"^ +$", x)

def read_text_file(path: str) -> str:
    with open(path, 'r', encoding="utf-8") as file_connection:
        content = file_connection.read()
    return content


def read_lrtemplate(path: str) -> str:
    template = read_text_file(path)
    #template = parse_lrtempalte(template)
    return template


def tokenizer(input_string: str) -> List[str]:
    candidates = ['"', '=', '{', '}', ',']
    break_points = list()
    for i in range(len(input_string)):
        current_char = input_string[i]
        if current_char in candidates:
            break_points.append(i)
        if current_char == "f" and (i + 1) < len(input_string):
            next_char = input_string[i + 1]
            if next_char in ['"', "'"]:
                break_points.append(i)

    if len(break_points) == 0:
        return [input_string]

    tokens = list()
    last_index = 0
    for index in break_points:
        tokens.append(input_string[last_index:index])
        tokens.append(input_string[index:(index+1)])
        last_index = index + 1

    tokens.append(input_string[last_index:])
    return list(filter(is_not_blank, tokens))







class ParserCache:
    '''Class that represents a cache to store the current state of the parser.'''
    def __init__(self, tokens: List[str]) -> None:
        self.ast = list()
        self.tokens = tokens
        self.index = 0
        if len(tokens) > 0:
            self.token = tokens[self.index]
        else:
            self.token = None
        return

    def len(self) -> int:
        return len(self.tokens)

    def current_token(self) -> str:
        return self.token

    def current_index(self) -> int:
        return self.index

    def next_token(self) -> None:
        self.index += 1
        if self.index < len(self.tokens):
            self.token = self.tokens[self.index]
        return

def parse_lrtempalte(text: str):
    tokens = tokenizer(text)
    parser_cache = ParserCache(tokens)
    parsing_result = _parse_input(parser_cache)
    return parsing_result.ast


def _parse_input(parser_cache: ParserCache) -> ParserCache:
    if parser_cache.len() == 0:
        return parser_cache

    if parser_cache.current_token() == '"':
        parser_cache = _parse_string(parser_cache)
    elif parser_cache.current_token() == '{':
        parser_cache = _parse_object(parser_cache)
    elif parser_cache.current_token() == '=':
        parser_cache = _parse_key_value_pair(parser_cache)
    else:
        parser_cache = _parse_value(parser_cache)

    parser_cache.next_token()
    if parser_cache.current_index() <= parser_cache.len() - 1:
        parser_cache = _parse_input(parser_cache)

    return parser_cache




def _parse_value(parser_cache: ParserCache) -> ParserCache:
    parser_cache.ast.append({
        'type': 'VALUE',
        'value': str(parser_cache.current_token())
    })
    return parser_cache

def _parse_string(parser_cache: ParserCache) -> ParserCache:
    parser_cache.next_token()
    # Add a placeholder in the top of the AST
    parser_cache.ast.append({
        'type': 'STRING',
        'value': list()
    })

    while parser_cache.current_index() < parser_cache.len() - 1:
        if parser_cache.current_token() == '"':
            break
        
        elem_ref = parser_cache.ast[-1]
        elem_ref['value'].append(parser_cache.current_token())
        parser_cache.next_token()
    
    return parser_cache



def _parse_object(parser_cache: ParserCache) -> ParserCache:
    parser_cache.next_token()
    object_elements = list()
    object_level = 0

    while parser_cache.current_index() < parser_cache.len() - 1:
        if object_level == 0 and parser_cache.current_token() == '}':
            break

        if parser_cache.current_token() == '{':
            object_level += 1
        if parser_cache.current_token() == '}':
            object_level -= 1
        
        object_elements.append(parser_cache.current_token())
        parser_cache.next_token()
    
    object_parser_cache = ParserCache(object_elements)
    object_parsed = _parse_input(object_parser_cache)
    return object_parsed.ast



def _parse_key_value_pair(parser_cache: ParserCache) -> ParserCache:
    left_operand = parser_cache.ast[-1]
    del parser_cache.ast[-1]
    parser_cache.next_token()

    value_tokens = list()
    if parser_cache.current_token() == '"':
        parser_cache.next_token()
        while parser_cache.current_index() < parser_cache.len() - 1:
            if parser_cache.current_token() == '"':
                value_tokens.append(parser_cache.current_token())
                break
            
            value_tokens.append(parser_cache.current_token())
            parser_cache.next_token()
        
        string_parser_cache = ParserCache(value_tokens)
        string_parsed = _parse_input(string_parser_cache)
        right_operand = string_parsed.ast
        

    elif parser_cache.current_token() == '{':
        parser_cache.next_token()
        object_level = 0
        while parser_cache.current_index() < parser_cache.len() - 1:
            if object_level == 0 and parser_cache.current_token() == '}':
                value_tokens.append(parser_cache.current_token())
                break

            if parser_cache.current_token() == '{':
                object_level += 1
            if parser_cache.current_token() == '}':
                object_level -= 1
            
            value_tokens.append(parser_cache.current_token())
            parser_cache.next_token()
        
        object_parser_cache = ParserCache(value_tokens)
        object_parsed = _parse_input(object_parser_cache)
        right_operand = object_parsed.ast


    else:
        right_operand = _parse_value(parser_cache.current_token())

    parser_cache.ast.append({
        'type': 'KV_PAIR',
        'left_operand': left_operand,
        'right_operand': right_operand
    })
    return parser_cache



t = read_lrtemplate("assets/example_template.lrtemplate")
print(parse_lrtempalte(t))