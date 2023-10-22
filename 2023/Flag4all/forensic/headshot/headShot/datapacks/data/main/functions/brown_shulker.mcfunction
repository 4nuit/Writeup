advancement revoke @s only custom:brown_shulker
execute as @e[type=minecraft:shulker, name=brown, nbt=!{ Color: 12 }] run data merge entity @s { Color: 12 }
