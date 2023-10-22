advancement revoke @s only custom:pink_shulker
execute as @e[type=minecraft:shulker, name=pink, nbt=!{ Color: 6 }] run data merge entity @s { Color: 6 }
