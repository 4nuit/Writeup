advancement revoke @s only custom:blue_shulker
execute as @e[type=minecraft:shulker, name=blue, nbt=!{ Color: 11 }] run data merge entity @s { Color: 11 }
