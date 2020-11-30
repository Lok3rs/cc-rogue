import simpleaudio as sa

wav = sa.WaveObject.from_wave_file

SOUNDS = {

    'sword': [wav('components/sound/sword_attack_1.wav'), wav('components/sound/sword_attack_2.wav')],
    'crit': wav('components/sound/crit_1.wav'),
    'die': wav('components/sound/die.wav'),
    'level_up': wav('components/sound/level_up.wav'),
    'game_over': [wav('components/sound/game_over_1.wav'), wav('components/sound/game_over_2.wav')],
    'pick_up': wav('components/sound/pick_up.wav'),
    'weapon': wav('components/sound/knife_ring.wav'),
    'food': wav('components/sound/food.wav'),
    'armor': wav('components/sound/armor.wav'),
    'inv': wav('components/sound/inv.wav')

}
