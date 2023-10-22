advancement revoke @s only custom:yellow_shulker
execute as @e[type=minecraft:shulker, name=yellow, nbt=!{ Color: 4 }] run data merge entity @s { Color: 4 }
