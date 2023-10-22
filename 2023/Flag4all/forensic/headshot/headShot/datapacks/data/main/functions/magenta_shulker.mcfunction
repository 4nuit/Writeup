advancement revoke @s only custom:magenta_shulker
execute as @e[type=minecraft:shulker, name=magenta, nbt=!{ Color: 2 }] run data merge entity @s { Color: 2 }
