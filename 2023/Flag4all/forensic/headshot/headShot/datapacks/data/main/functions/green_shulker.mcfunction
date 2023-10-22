advancement revoke @s only custom:green_shulker
execute as @e[type=minecraft:shulker, name=green, nbt=!{ Color: 13 }] run data merge entity @s { Color: 13 }
