obs = obslua

-- Tempo total da gravação em segundos (3h 40min 7s = 13207 segundos)
duration = 13210

function script_description()
    return "Inicia a gravação automaticamente e para após 3h 40min 10s (13210 segundos)."
end

function start_recording()
    obs.obs_frontend_recording_start()
    obs.timer_add(stop_recording, duration * 1000)
end

function stop_recording()
    obs.timer_remove(stop_recording)
    obs.obs_frontend_recording_stop()
end

function script_load(settings)
    start_recording()
end
