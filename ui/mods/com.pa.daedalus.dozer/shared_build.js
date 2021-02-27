var newBuild = {
"/pa/units/paeiou/dozer/dozer.json": ["vehicle", 0,{ row: 0, column: 5, titans: true }],

}
if (Build && Build.HotkeyModel && Build.HotkeyModel.SpecIdToGridMap) {
_.extend(Build.HotkeyModel.SpecIdToGridMap, newBuild);
}