"""

"""
import os
popup = op("popDialog")


class ToxExporter:


	def __init__(self):
		return

	def ExportTox(self):
		self.source_op = parent().par.Targetop.eval()
		self.module_name = self.source_op.par.Modulename.eval()
		print(f"Export tox from \"{self.source_op.name}\" to \"{self.module_name}\"")


		# create copy
		root_path = os.path.dirname(parent().path)
		preexisting = op(os.path.join(root_path, self.module_name))
		if preexisting:
			raise ValueError('The source base may not have the same name as the exported module name')


		copy = op(root_path).copy(self.source_op)
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
		if not os.path.exists(parent().par.Exportlocation.eval()):
			os.makedirs(parent().par.Exportlocation.eval())
		outComp.save(os.path.join(parent().par.Exportlocation.eval(), outComp.par.Modulename + ".tox"))
		outComp.destroy()
		# create popup so the user knows something happened
		popup.par.Text = "Created tox \"{}\" at \"{}\"".format(self.module_name, os.path.abspath(parent().par.Exportlocation.eval()).replace('\\', '/'))
		popup.par.Open.pulse()

	def ConvertExternalToLocal(self, outComp):
		debug("convert to local")
		for child in outComp.children:	
			if child.family == "DAT":
				print(child)
				if child.par["file"] and child.par["file"].mode != ParMode.EXPRESSION:
					print(child.par["file"].mode)
					child.par.file = ""
				if child.par["syncfile"] and child.par["syncfile"].mode != ParMode.EXPRESSION:
					child.par.syncfile = False

	def RemoveDev(self, outComp):
		for child in outComp.children:	
			if "dev" in child.tags:
				child.destroy()
