var resources = {
  badges: {
  data: {
    'WIN_GOLD': {
      img: '/static/img/badges/badge-gold.png',
      name: 'Top 1',
      desc: 'You finished 1st'},
    'WIN_SILVER': {
      img: '/static/img/badges/badge-silver.png',
      name: 'Top 2',
      desc: 'You finished 2nd'},
    'WIN_BRONZE': {
      img: '/static/img/badges/badge-bronze.png',
      name: 'Top 3',
      desc: 'You finished 3rd'},
    'WIN_ALMOST': {
      img: '/static/img/badges/win_wooden.svg',
      name: 'Almost won',
      desc: 'You finished 4th'},
    'RISING_STAR': {
      img: '/static/img/badges/sea-star.svg',
      name: 'Rising star',
      desc: 'Got 0 <= ratio <= 0.1'},
    'GAUNTLET_KILL': {
      img: '/static/img/badges/circular-sawblade.svg',
      name: 'Butcher',
      desc: 'You killed an opponent with Gauntlet'},
    'DEATH': {
      img: '/static/img/badges/topdeaths.svg',
      name: 'Crap like me',
      desc: 'You got killed'},
    'KILLING_SPREE': {
      img: '/static/img/badges/icicles-aura.svg',
      name: 'Excellent',
      desc: 'You killed two opponents within 2 seconds'},
    'GAUNTLET_DEATH': {
      img: '/static/img/badges/swine.svg',
      name: 'Humiliation',
      desc: 'You got killed with Gauntlet'},
    'HEADHUNTER': {
      img: '/static/img/badges/crowned-skull.svg',
      name: 'Headhunter',
      desc: 'You killed highest score player with Gauntlet'},
    'DUCKHUNTER': {
      img: '/static/img/badges/surprised-skull.svg',
      name: 'Duckhunter',
      desc: 'You killed lowest score player with Gauntlet'},
    'SELFKILL': {
      img: '/static/img/badges/emo.png',
      name: 'Black matters',
      desc: 'You killed yourself'},
    'KILLING_SPREE_R': {
      img: '/static/img/badges/placeholder.png',
      name: 'Killing Spree',
      desc: 'You killed that many without dying'},
    'DYING_SPREE': {
      img: '/static/img/badges/dyingspree.png',
      name: 'Dying Spree',
      desc: 'You died that many times without a kill'},
    'LAVASAURUS': {
      img: '/static/img/badges/badge-lavasaurus.png',
      name: 'Lavasaurus',
      desc: 'You died in LAVA!'}
  }
  },

  weapons: {
    'ROCKET_SPLASH': {
      img: '/static/img/weapons/icona_rocket.svg'
    },
    'ROCKET': {
      img: '/static/img/weapons/icona_rocket.svg'
    },
    'GRENADE': {
      img: '/static/img/weapons/icona_grenade.svg'
    },
    'GRENADE_SPLASH': {
      img: '/static/img/weapons/icona_grenade.svg'
    },
    'PLASMA': {
      img: '/static/img/weapons/icona_plasma.svg'
    },
    'MACHINEGUN': {
      img: '/static/img/weapons/icona_machinegun.svg'
    },
    'SHOTGUN': {
      img: '/static/img/weapons/icona_shotgun.svg'
    },
    'GAUNTLET': {
      img: '/static/img/weapons/icona_gauntlet.png'
    },
    'BFG': {
      img: '/static/img/weapons/icona_bfg.png'
    },
    'BFG_SPLASH': {
      img: '/static/img/weapons/icona_bfg.png'
    },
    'LIGHTNING': {
      img: '/static/img/weapons/icona_lightning.svg'
    },
    'RAILGUN': {
      img: '/static/img/weapons/icona_railgun.svg'
    },
    'FALLING': {
      img: '/static/img/weapons/falling.svg'
    },
    'LAVA': {
      img: '/static/img/weapons/lava.svg'
    }
  }
}

resources.badges.getInfo = (badgeName) => {
  badgeInfo = context.resources.badges.data[badgeName]
  if (badgeInfo) {
    return badgeInfo
  } else {
    return {
      img: '',
      desc: 'missing',
      name: badgeName
    }
  }
}

resources.badges.getMedalNames = () => {
  res = []
  for (key of Object.keys(resources.badges.data)) {
    res.push({'name': key})
  }
  return res
}

context.resources = resources
