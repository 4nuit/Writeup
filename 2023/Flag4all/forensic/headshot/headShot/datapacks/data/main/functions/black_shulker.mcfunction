advancement revoke @s only custom:black_shulker
execute as @e[type=minecraft:shulker, name=black, nbt=!{ Color: 15 }] run data merge entity @s { Color: 15 }
