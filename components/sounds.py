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
    'inv': wav('components/sound/inv.wav'),
    'bump': wav('components/sound/bump.wav'),
    'monster': [
        wav('components/sound/shade1.wav'), wav('components/sound/shade2.wav'),
        wav('components/sound/shade3.wav'), wav('components/sound/shade4.wav'),
        wav('components/sound/shade5.wav'), wav('components/sound/shade6.wav'),
        wav('components/sound/shade7.wav'), wav('components/sound/shade8.wav'),
        wav('components/sound/shade9.wav'), wav('components/sound/shade10.wav'),
        wav('components/sound/shade11.wav'), wav('components/sound/shade12.wav'),
        wav('components/sound/shade13.wav'), wav('components/sound/shade14.wav'),
        wav('components/sound/shade15.wav'), wav('components/sound/ogre3.wav'),
        wav('components/sound/ogre4.wav'), wav('components/sound/giant1.wav'),
        wav('components/sound/giant5.wav'), wav('components/sound/giant3.wav')
    ],

}
