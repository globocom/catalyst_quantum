from quantum.openstack.common import cfg


database_opts = [
    cfg.StrOpt('sql_connection', default='sqlite://'),
    cfg.IntOpt('sql_max_retries', default=-1),
    cfg.IntOpt('reconnect_interval', default=2),
]


cfg.CONF.register_opts(database_opts, "DATABASE")
