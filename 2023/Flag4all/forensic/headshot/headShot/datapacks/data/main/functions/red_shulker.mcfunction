advancement revoke @s only custom:red_shulker
execute as @e[type=minecraft:shulker, name=red, nbt=!{ Color: 14 }] run data merge entity @s { Color: 14 }
