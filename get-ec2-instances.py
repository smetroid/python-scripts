#!/usr/bin/python3
import boto3
import boto3.session
import json
#from ec2data import *

### CONSTANTS

### FUNCTIONS
def get_instances(region="us-east-1"):
	"""Get instance information

	Args:
		region (string): string to retrieve ec2 instances from

	Returns:
		Dictionary: dictionary of images ids as keys and instance ids as values
	"""

	instance_info = {}
	try:
		ec2 = boto3.client("ec2", region)

		token = ""
		while True:
			# Setting MaxResults to test the while loop -EC-
			data = ec2.describe_instances(MaxResults=5,NextToken=token)
			#data = ec2_data
			for r in data["Reservations"]:
				for instance in r["Instances"]:
					# Check to see if the imageId is already part of the dictionary instance_info
					image_id = instance["ImageId"]
					instance_id = instance["InstanceId"]
					if image_id in instance_info:
						instance_ids = instance_info[image_id]
						instance_ids.append(instance_id)
						instance_info[image_id] = instance_ids
					else:
						instance_info[image_id] = [instance_id]

			token = data.get('NextToken')
			if not token:
				break

	except Exception as e:
		print("Error in get_instances function")
		print(str(e))
		exit(1)

	return instance_info


def get_ami_info(image, instance_ids):
	"""Get AWS ami information

	Args:
		image (dictionary): ami data returned from ec2 describe images function
		instance_ids (list): list of instances associated with the ami

	Returns:
		dictionary: list of specific AMI fields

	"""

	ami_fields = ["ImageId","Description","ImageName","ImageLocation","OwnerId","InstanceIds"]
	image_info = {}
	
	try:
		for field in ami_fields:
			if field == "ImageName":
				image_info[field] = image["Name"]
			elif field == "InstanceIds":
				image_info[field] = instance_ids
			else:
				image_info[field] = image[field]
	except:
		for field in ami_fields:
			if field == "InstanceIds":
				image_info[field] = instance_ids
			else:
				image_info[field] = None

	return image_info


def get_images(instance_info):
	"""Get image descriptions

	Args:
		instance_info (dictionary): dictionary containing the image ids and the instances ids associated with the image
	"""
	ec2 = boto3.client("ec2", "us-east-1")

	data = ""
	ami_data = {}
	
	try:
		image_ids = list(instance_info.keys())

		# Get image information found based on instances
		data = ec2.describe_images(ImageIds=image_ids)
		for image in data["Images"]:
			image_id = image["ImageId"]
			instance_ids = instance_info[image_id]
			ami_data[image_id] = get_ami_info(image, instance_ids)
		
		# Set nulls for AMIs no longer available
		for id in image_ids:
			instance_ids = instance_info[id]
			if id not in ami_data:
				ami_data[id] = get_ami_info(id, instance_ids)

	except Exception as e:
		print("Error in get_images function")
		print(str(e))
		exit(1)

	return ami_data


def main():
	"""Entry point into the script """
	instance_info = get_instances()
	data = get_images(instance_info)
	print(json.dumps(data, indent=2))


if __name__ == "__main__":
	main()
