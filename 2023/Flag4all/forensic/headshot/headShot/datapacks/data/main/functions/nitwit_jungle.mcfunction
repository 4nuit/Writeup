advancement revoke @s only custom:nitwit_jungle
execute as @e[type=minecraft:villager, name=nitwit, nbt={VillagerData:{type:'minecraft:jungle', profession:'minecraft:none'}}] run data merge entity @s {VillagerData:{type:'minecraft:jungle', profession:'minecraft:nitwit'}}
