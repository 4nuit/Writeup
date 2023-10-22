advancement revoke @s only custom:nitwit_snow
execute as @e[type=minecraft:villager, name=nitwit, nbt={VillagerData:{type:'minecraft:snow', profession:'minecraft:none'}}] run data merge entity @s {VillagerData:{type:'minecraft:snow', profession:'minecraft:nitwit'}}
