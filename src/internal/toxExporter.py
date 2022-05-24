"""

"""
import os
popup = op("popDialog")


class ToxExporter:


	def __init__(self):
		pass

	def ExportTox(self):
		self.source_op = parent().par.Targetop.eval()
		self.module_name = self.source_op.par.Modulename.eval()
		print("Export tox from", self.source_op.name, "to", self.module_name)


		# create copy
		preexisting = op("/" + self.module_name)
		print(preexisting)
		if preexisting:
			if "source" not in preexisting.tags:
				preexisting.destroy()
			else:
				raise ValueError('The source base may not have the same name as the exported module name')


		copy = op("/").copy(self.source_op)
		copy.name = self.module_name
		copy.nodeX = parent().nodeX + 300

		# convert dats
		self.ConvertExternalToLocal(copy)
		self.RemoveDev(copy)



		# export
		self.SaveTox(copy)

	def SaveTox(self, outComp):
		# remove color
		outComp.color = me.color
		# remove tags
		outComp.tags = []
		# write file
		outComp.save(os.path.join(parent().par.Exportlocation.eval(), outComp.par.Modulename + ".tox"))
		outComp.destroy()
		popup.par.Text = "Created tox \"{}\" at \"{}\"".format(self.module_name, os.path.abspath(parent().par.Exportlocation.eval()).replace('\\', '/'))
		popup.par.Open.pulse()

	def ConvertExternalToLocal(self, outComp):
		for child in outComp.children:	
			if child.family == "DAT":
				print("Process DAT", child.name)
				child.par.file = ""
				child.par.syncfile = False

	def RemoveDev(self, outComp):
		for child in outComp.children:	
			if "dev" in child.tags:
				child.destroy()
