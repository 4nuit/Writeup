advancement revoke @s only custom:nitwit_savanna
execute as @e[type=minecraft:villager, name=nitwit, nbt={VillagerData:{type:'minecraft:savanna', profession:'minecraft:none'}}] run data merge entity @s {VillagerData:{type:'minecraft:savanna', profession:'minecraft:nitwit'}}
