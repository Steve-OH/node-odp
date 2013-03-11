{
	'targets': [
		{
			'target_name': 'odpnode',
			'sources': [ 
				'src/helpers/helpers.cc',
				'odpnode.cc',
				'src/odpconnection.cc',
				'src/odpcommand.cc',
				'src/odpdata.cc'
			],
			'conditions' : [
				['OS=="win"', {
					'defines': [
						'PLATFORM="win32"'
					],
					'cflags': [
						'/clr',
					],
					'msvs_settings': {
						'VCCLCompilerTool': {	
							'AdditionalOptions':[
								'/clr'
							],
						},
					},
					'configurations':{
						'Debug':{
							'msvs_settings': {
								'VCCLCompilerTool': {
									'RuntimeLibrary': '3',
									'RuntimeTypeInfo': 'true',
									'AdditionalUsingDirectories': '../dependencies',
								},
							},
						},
						'Release': {
							'msvs_settings': {
								'VCCLCompilerTool': {
									'RuntimeLibrary': '3',
									'RuntimeTypeInfo': 'true',
									'AdditionalUsingDirectories': '../dependencies',
								},
								'VCLinkerTool': {
									'AdditionalLibraryDirectories': [
										'../dependencies'
									]
								}
							},
						},
					},	
				}],
			],
		},
	],
}