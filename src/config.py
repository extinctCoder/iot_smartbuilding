from dynaconf import Dynaconf


settings = Dynaconf(
    warn_dynaconf_global_settings=True,
    environments=True,
    lowercase_read=False,
    load_dotenv=True,
    envvar_prefix="APP",
    settings_files=["conf/settings.yaml", "conf/development.yaml"],
)

if settings.DEBUG:
    settings.configure(FORCE_ENV_FOR_DYNACONF="development")
else:
    settings.configure(FORCE_ENV_FOR_DYNACONF="production")
