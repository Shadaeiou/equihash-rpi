{
  "targets": [
    {
      "target_name": "khovratovich",
      "sources": [
        "lib/khovratovich/addon.cc",
        "lib/khovratovich/pow.cc",
        "lib/khovratovich/blake/blake2b.c"
      ],
      "include_dirs": ["<!(node -e \"require('nan')\")"],
      "cflags": [
        #"-m64",
        #"-maes",
        #"-mavx",
        "-Wno-maybe-uninitialized",
        "-std=c++11",
        "-march=armv7-a",
        "-mfpu=neon-vfpv4",
        "-mfloat-abi=hard"
      ]
    }
  ]
}
