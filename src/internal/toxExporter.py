"""

"""
import os


class ToxExporter:


	def __init__(self):
		pass

	def ExportTox(self):
		self.source_op = parent().par.Targetop.eval()
		self.module_name = self.source_op.par.Modulename
		print("Export tox from", self.source_op.name, "to", self.module_name)


		# create copy
		copy = op("/").copy(self.source_op)
		copy.name = self.module_name
		copy.nodeX = parent().nodeX + 300

		# convert dats
		self.ConvertExternalToLocal(copy)



		# export
		self.SaveTox(copy)

	def SaveTox(self, outComp):
		outComp.save(os.path.join(parent().par.Exportlocation.eval(), outComp.par.Modulename + ".tox"))
		outComp.destroy()

	def ConvertExternalToLocal(self, outComp):
		for child in outComp.children:	
			if child.family == "DAT":
				print("Process DAT", child.name)
				child.par.file = ""
				child.par.syncfile = False
