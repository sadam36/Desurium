{
	'includes': [
		 '../../../build_lin/common.gypi',
	],
	'targets': [
	{
		'target_name': 'uicore',
		'type': 'shared_library',
		'dependencies' : [
			'<(shared_dir)/mcfcore/mcfcore.gyp:mcfcore',
			'<(shared_dir)/usercore/usercore.gyp:usercore',
			'<(static_dir)/wx_controls/wx_controls.gyp:wx_controls',
			'<(static_dir)/managers/managers.gyp:*',
			'<(static_dir)/util_thread/util_thread.gyp:threads',
			'<(static_dir)/util_fs/util_fs.gyp:util_fs',
			'<(static_dir)/util/util.gyp:*',
			'<(static_dir)/ipc_pipe/ipc_pipe.gyp:ipc_pipe',
			'<(static_dir)/umcf/umcf.gyp:umcf',
			'<(third_party_dir)/sqlite/sqlite.gyp:sqlite',
			'<(third_party_dir)/sqlite3x/sqlite3x.gyp:sqlite3x',
			'<(third_party_dir)/tinyxml/tinyxml.gyp:tinyxml',
			'<(third_party_dir)/libs.gyp:wxWidgets',	
			'<(common_dir)/gcJSBase.gyp:gcJSBase',
		],
		'include_dirs': [
			'./RES',
			'./code',
		],
		'defines' : [
			'UI_HIDE_MODS',
			'ENABLE_SEARCH',
		],
		'sources': [
			'code/AboutPageDev.cpp',
			'code/AboutPageMain.cpp',
			'code/AboutForm.cpp',
			'code/BaseInstallPage.cpp',
			'code/BaseMenuButton.cpp',
			'code/BasePage.cpp',
			'code/BaseTabPage.cpp',
			'code/BaseToolBarControl.cpp',
			'code/BreadCrumb.cpp',
			'code/ButtonStrip.cpp',
			'code/CDKeyForm.cpp',
			'code/CDKInfo.cpp',
			'code/CDKProgress.cpp',
			'code/ChangeLogForm.cpp',
			'code/ComplexPrompt.cpp',
			'code/Console.cpp',
			'code/CreateForm.cpp',
			'code/CreateInfoPage.cpp',
			'code/CreateOVPage.cpp',
			'code/CreateProgPage.cpp',
			'code/DesuraControl.cpp',
			'code/DesuraServiceError.cpp',
			'code/DispLoading.cpp',
			'code/DStripMenuControls.cpp',
			'code/EulaForm.cpp',
			'code/ExeSelectForm.cpp',
			'code/FrameButtons.cpp',
			'code/GameDiscForm.cpp',
			'code/gcImgLoader.cpp',
			'code/gcJSBinding.cpp',
			'code/gcJSBranchInfo.cpp',
			'code/gcJSEvents.cpp',
			'code/gcJSItemInfo.cpp',
			'code/gcJSLinks.cpp',
			'code/gcJSSettings.cpp',
			'code/gcJSUploads.cpp',
			'code/gcJSUserInfo.cpp',
			'code/gcMiscWebControl.cpp',
			'code/gcSchemeBase.cpp',
			'code/gcThemeLoader.cpp',
			'code/gcUpdateForm.cpp',
			'code/gcWCEvents.cpp',
			'code/gcWCEvents_js.cpp',
			'code/gcWCUtil.cpp',
			'code/gcWebControl.cpp',
			'code/gcWebFakeBrowser.cpp',
			'code/HtmlTabPage.cpp',
			'code/HtmlToolBarControl.cpp',
			'code/ICheckFinishPage.cpp',
			'code/ICheckProgressPage.cpp',
			'code/InstallBannerPage.cpp',
			'code/InstallBranch.cpp',
			'code/InstallDLPage.cpp',
			'code/InstallDLToolPage.cpp',
			'code/InstallDVPage.cpp',
			'code/InstallGIPage.cpp',
			'code/InstallINCPage.cpp',
			'code/InstallINPage.cpp',
			'code/InstallINToolPage.cpp',
			'code/InstallPrompt.cpp',
			'code/InstallVInfoPage.cpp',
			'code/InstallVIPage.cpp',
			'code/InstallWaitPage.cpp',
			'code/InternalLink.cpp',
			'code/ItemForm.cpp',
			'code/ItemTabPage.cpp',
			'code/ItemToolBarControl.cpp',
			'code/ItemUpdateForm.cpp',
			'code/LaunchPrompt.cpp',
			'code/Log.cpp',
			'code/LoginForm.cpp',
			'code/UICoreMain.cpp',
			'code/MainForm.cpp',
			'code/MainFormCustomFrame.cpp',
			'code/MainFormLeftBorder.cpp',
			'code/MainMenuButton.cpp',
			'code/MainApp.cpp',
			'code/MainApp_cvar.cpp',
			'code/MainApp_internal.cpp',
			'code/MainApp_wildcards.cpp',
			'code/Managers.cpp',
			'code/MenuFiller.cpp',
			'code/MenuSeperator.cpp',
			'code/MenuStrip.cpp',
			'code/ModWizard.cpp',
			'code/ModWizardFinPage.cpp',
			'code/ModWizardInfoPage.cpp',
			'code/ModWizardProgPage.cpp',
			'code/NewsForm.cpp',
			'code/PasswordReminder.cpp',
			'code/PreloadPage.cpp',
			'code/SearchControl.cpp',
			'code/SteamUser.cpp',
			'code/StripMenuButton.cpp',
			'code/TabButton.cpp',
			'code/TabControl.cpp',
			'code/TaskBarIcon.cpp',
			'code/TaskBarIcon_Ballon.cpp',
			'code/TaskBarIcon_Icon.cpp',
			'code/TBI_BaseMenu.cpp',
			'code/TBI_GameMenu.cpp',
			'code/TBI_UpdateMenu.cpp',
			'code/TBI_WindowMenu.cpp',
			'code/UICoreEntry.cpp',
			'code/UninstallInfoPage.cpp',
			'code/UninstallProgressPage.cpp',
			'code/UploadForm.cpp',
			'code/UploadInfoPage.cpp',
			'code/UploadProgPage.cpp',
			'code/UploadPrompt.cpp',
			'code/UsernameBox.cpp',
			'code/NewAccountDialog.cpp',
		],
		'conditions' : [
			['desura_nongpl==1',{
				'dependencies' : [
					'<(desura_nongpl_dir)/shared/uicore/uicore.gyp:uicore_nongpl',
				]
			}]
		],
	}],
}