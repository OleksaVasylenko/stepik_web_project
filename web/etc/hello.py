CONFIG = {
  'mode': 'wsgi',
  'python': '/usr/bin/python',
  'working_dir': '/home/box/web',
  'args': (
    '--bind=0.0.0.0:8000',
    '--workers=2',
    '--timeout=15',
    '--log-level=debug',
    'ask.wsgi:application',
  ),
}