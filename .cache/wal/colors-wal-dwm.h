static const char norm_fg[] = "#c2c6c7";
static const char norm_bg[] = "#0c1d21";
static const char norm_border[] = "#485558";

static const char sel_fg[] = "#c2c6c7";
static const char sel_bg[] = "#3571aa";
static const char sel_border[] = "#c2c6c7";

static const char urg_fg[] = "#c2c6c7";
static const char urg_bg[] = "#3d94a9";
static const char urg_border[] = "#3d94a9";

static const char *colors[][3]      = {
    /*               fg           bg         border                         */
    [SchemeNorm] = { norm_fg,     norm_bg,   norm_border }, // unfocused wins
    [SchemeSel]  = { sel_fg,      sel_bg,    sel_border },  // the focused win
    [SchemeUrg] =  { urg_fg,      urg_bg,    urg_border },
};
