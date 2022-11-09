#!/usr/bin/env python

import click
import requests

@click.command()
@click.option('--token', required=True, prompt=True, 
    help='Your Gitlab personal access token')
@click.option('--repo', required=True, prompt=True, 
    type=click.Choice(['template','premium_template']), 
    help='The repository you want to fork')
@click.option('--name', required=True, prompt=True, 
    type=str, 
    help='The name you would like the new fork to be called. This will also be the project slug')
@click.option('--namespace', required=True, prompt=True, 
    help='The namespace you would like to fork the project to.')

def fork_repo(token, repo, name, namespace):
    click.echo(f'Going to fork {repo} as {name} into {namespace}')

    if repo ==  'template':
        url = 'https://gitlab.example.com/api/v4/projects/1/fork'
    elif repo ==  'premium_template':
        url = 'https://gitlab.example.com/api/v4/projects/2/fork'
    else:
        print('Ooops, something isn\'t working...')

    params = {'name': name, 
              'private_token': token,
              'path': name,
              'namespace': namespace }

    r = requests.post(url, params = params)

    if r:
        print('Success! Link to new fork: ', r.json().get("web_url"))
    else:
        print('That didn\'t work... \nStatus code: ', r.status_code)

if __name__ == '__main__':
    fork_repo(auto_envvar_prefix='FORK')