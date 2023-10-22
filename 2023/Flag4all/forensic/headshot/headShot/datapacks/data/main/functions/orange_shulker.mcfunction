advancement revoke @s only custom:orange_shulker
execute as @e[type=minecraft:shulker, name=orange, nbt=!{ Color: 1 }] run data merge entity @s { Color: 1 }
